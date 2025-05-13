from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class HydrationRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hydration_records')
    date = models.DateField(auto_now_add=True)
    amount = models.PositiveIntegerField(default=0)  # En vasos (1 vaso = 250ml)
    goal = models.PositiveIntegerField(default=8)     # Meta diaria en vasos

    class Meta:
        unique_together = ('user', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.email} - {self.date}: {self.amount}/{self.goal}"

class HydrationReminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hydration_reminders')  # Añadido related_name
    time = models.TimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Recordatorio para {self.user.email} a las {self.time}"

    class Meta:
        ordering = ['time']

class HydrationStats(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='hydration_stats',
        primary_key=True
    )
    current_streak = models.PositiveIntegerField(default=0)
    longest_streak = models.PositiveIntegerField(default=0)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user.email}: Streak {self.current_streak} (Record: {self.longest_streak})"