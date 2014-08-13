/*Metrónomo de pranyama.
# Recebe como imput tempo de exalação, tempo de inalação e tempo de apeneia.
# Mostra um círculo com perímetro tempototal (medido em segundos)
# Em cima mostra "inhale" "exhale" ou "hold" e em baixo um ponteiro dá a volta a secções de círculo coloridos, consoante a actividade*/

var inhale = 20;
var exhale = 10;
var apneia = 0;
var totaltime = inhale + exhale + 2 * apneia;


//holds the current second as displayed on the clock
var current = 0;
var state = "";
var total = 0;

function formater (seconds) {
	str = "";
	second = seconds%60
	minute = Math.floor(seconds/60)
	str = "Time elapsed " + minute + ":" + second;
	return str 
}

function augment () {
	//updates clock by augmenting it one unit
	current = current%totaltime;
	current += 1;
	total += 1;
	if (current <= inhale) {
		if (current == inhale) {
			//playsoundsound();
		}
		state = "Inhale";
	}
	else if (current > inhale && current <= inhale + apneia)
		state = "Apnea";
	else if (current > inhale + apneia && current <= inhale + apneia + exhale){		
		if (current == inhale + apneia + exhale) {
			//sound	
		}
		state = "Exhale";
	}
	else
		state = "Apnea";
	console.log(current + " " + state + "                               " + formater(total));
}

setInterval(augment,1000);
