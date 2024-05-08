// Random

// function setup(){
// 	createCanvas(400, 400)
// 	background(0)
// }

// function draw(){
	
// 	translate(width/2, height/2)

// 	// let v = createVector(random(-100, 100), random(-100, 100))
// 	v = p5.Vector.random2D()
// 	v.mult(random(50, 100))

// 	strokeWeight(4)
// 	stroke(255, 50)
// 	line(0, 0, v.x, v.y)
// }

//Mover

function setup(){
	createCanvas(600, 600)

}

function draw(){
	background(0)
	let pos = createVector(300, 300)
	let mouse = createVector(mouseX, mouseY)

	let v = p5.Vector.sub(mouse,pos)
	// let m = v.mag()
	// v.div(m)
	// v.mult(50)
	// v.normalize()
	v.setMag(50)

	translate(width/2, height/2)
	strokeWeight(4)
	stroke(255, 50)
	line(0, 0, v.x, v.y)
}
