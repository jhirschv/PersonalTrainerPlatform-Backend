from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView
from rest_framework.routers import DefaultRouter
from .views import (ProgramViewSet, PhaseViewSet, WorkoutViewSet, ExerciseViewSet, WorkoutExerciseViewSet, UserProgramViewSet, 
ProgramCreateView, ActiveProgramView, SetActiveProgramView, CurrentWorkoutView, StartWorkoutSessionView, WorkoutSessionDetailView, PhasesDetailView,
UpdateWorkoutProgressView, UserWorkoutSessionView, ExerciseSetViewSet)

router = DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'user_programs', UserProgramViewSet, basename='user_program')
router.register(r'phases', PhaseViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'workout_exercises', WorkoutExerciseViewSet)
router.register(r'user_workout_sessions', UserWorkoutSessionView, basename='userworkoutsession')

urlpatterns = [
    path('', include(router.urls)),
    path('create_program/', ProgramCreateView.as_view(), name='program-create'),
    path('get_active_program/', ActiveProgramView.as_view(), name='get_active_program'),
    path('set_active_program/', SetActiveProgramView.as_view(), name='set_active_program'),
    path('current_workout/', CurrentWorkoutView.as_view(), name='current_workout'),
    path('start_workout_session/', StartWorkoutSessionView.as_view(), name='start-workout-session'),
    path('workoutSession/<int:id>/', WorkoutSessionDetailView.as_view(), name='workout-session-detail'),
    path('phase_details/<int:program_id>/', PhasesDetailView.as_view(), name='phase_detail'),
    path('update_workout_progress/', UpdateWorkoutProgressView.as_view(), name='update_workout_progress'),
    path('exercise_set_update/<int:pk>/', ExerciseSetViewSet.as_view(), name='exercise_set_update'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
]

 