from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle
from .forms import VehicleForm

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.owner = request.user  
            vehicle.save()
            return redirect('vehicle_list')  
    else:
        form = VehicleForm()
    
    return render(request, 'add_vehicle.html', {'form': form})
def vehicle_list(request):
    vehicles = Vehicle.objects.filter(owner=request.user)
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})

def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk, owner=request.user)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})