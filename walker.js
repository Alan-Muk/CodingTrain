class Walker{
	constructor(x, y){
		this.pos = createVector(x, y);
		this.vel = p5.Vector.random2D()
		this.vel.mult(random(10))
	}

	update(){
		this.pos.add(this.vel);

	}

	show(){
		stroke(255);
		strokeWeight(2);
		fill(255, 100);
		ellipse(this.pos.x, this.pos.y, 32);

	}
}