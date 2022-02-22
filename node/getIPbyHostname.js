var dns = require("dns");

function hostnameLookup(hostname) {
	dns.lookup(hostname, function(err, addresses, family){
		console.log(addresses);
	});
}



var hostname = process.argv[2]

console.log(`Checking IP of: ${hostname}`);
hostnameLookup(hostname);
