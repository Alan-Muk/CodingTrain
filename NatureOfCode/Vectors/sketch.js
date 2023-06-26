let walker;

function setup(){
	createCanvas(400, 400);
	walker = new walker(200, 200);
	background(0);

}

function draw(){
	walker.update(); 
	walker.show();
}