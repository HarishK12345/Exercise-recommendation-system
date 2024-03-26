
function updateDuration() {
    var skillLevel = document.getElementById("skill-level").value;
    var durationField = document.getElementById("duration");

    switch (skillLevel) {
        case "beginner":
            durationField.value = "5-10 minutes";
            break;
        case "intermediate":
            durationField.value = "10-20 minutes";
            break;
        case "advanced":
            durationField.value = "20-30 minutes";
            break;
        default:
            durationField.value = "";
            break;
        }
}
