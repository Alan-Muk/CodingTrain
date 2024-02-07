
// Walker

// let walker;

// function setup() {
// 	createCanvas(400, 400);
// 	walker = new Walker(200, 200);
// }

// function draw() {
// 	background(51);
// 	walker.update(); 
// 	walker.show();

// }

// Mover

let mover;

function setup(){
	createCanvas(600, 600);
	mover = new Mover(300, 300);
}

function draw(){
	background(0)
	mover.update();
	mover.show();
}