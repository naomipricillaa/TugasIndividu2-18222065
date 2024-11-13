from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CalculationHistory

@login_required
def calculate_pressure(request):
    if request.method == 'POST':
        # Retrieve input values from the form
        volume = float(request.POST.get('volume'))
        mol = float(request.POST.get('mol'))
        suhu = float(request.POST.get('suhu'))

        # Perform the calculation (example: Ideal Gas Law)
        pressure = mol * 8.314 * suhu / volume  # P = nRT/V
        result = f"{pressure:.2f} Pa"

        # Check the number of history entries for this user
        user_history = CalculationHistory.objects.filter(user=request.user)
        if user_history.count() >= 5:
            # If there are already 5 entries, delete all history for the user
            user_history.delete()

        # Save the new calculation to the history
        CalculationHistory.objects.create(user=request.user, result=result)

        # Retrieve the latest 5 calculations for this user (will be 1 entry if reset)
        history = CalculationHistory.objects.filter(user=request.user).order_by('-created_at')[:5]

        # Pass the result and history to the template
        context = {
            'result': result,
            'history': history,
        }
        return render(request, 'calc.html', context)
    else:
        # On GET request, fetch only the history without performing a new calculation
        history = CalculationHistory.objects.filter(user=request.user).order_by('-created_at')[:5]
        return render(request, 'calc.html', {'history': history})
