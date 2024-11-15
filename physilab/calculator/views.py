from django.shortcuts import render, redirect
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

        # Save the new calculation to the history
        CalculationHistory.objects.create(user=request.user, result=result)

        # Retrieve all calculations for this user
        history = CalculationHistory.objects.filter(user=request.user).order_by('created_at')

        # Pass the result and history to the template
        context = {
            'result': result,
            'history': history,
        }
        return render(request, 'calc.html', context)
    else:
        # On GET request, fetch all history without performing a new calculation
        history = CalculationHistory.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'calc.html', {'history': history})

def clear_history(request):
    # Delete all calculation history for the logged-in user
    CalculationHistory.objects.filter(user=request.user).delete()
    # Redirect back to the calculator page (or wherever you want)
    return redirect('calc')