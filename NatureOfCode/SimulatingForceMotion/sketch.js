let mover;

function setup(){
	createCanvas(600, 600);
	mover = new Mover(300, 300);
}

function draw(){
	background(0)

	if (mouseIsPressed){
		let wind = createVector(0.2,0)
		mover.applyForce(wind)
	}

	let gravity = createVector(0, 0.3);
	mover.applyForce(gravity);
	

	mover.update();
	mover.edges();
	mover.show();
}