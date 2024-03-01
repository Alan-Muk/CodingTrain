function setup() {
	createCanvas(600, 600)
	p0 = createVector(0, 300)
	p1 = createVector(300, 0)
	p2 = createVector(600, 300)
}

function draw() {
	background(0)
	stroke(255)
	strokeWeight(4)
	
	beginShape()
	for(let t = 0; t <= 1; t += 0.1){
		let x1= lerp(p0.x. p1.x, t)
		let y1 = lerp(p0.y, p1.y, t)
		let x2 = lerp(p1.x, p2.x, t)
		let y2 = lerp(p1.y, p2.y, t)
		let x = lerp(x1)
	}

}