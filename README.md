# jwt-cracker
Script to crack a jwt.

# Usage
`python3 jwtCracker.py <jwt> <HashAlgorithm> <wordlist> <numberOfThreads>`

Example: 

`python3 jwtCracker.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyNjZ9.eACboSCOtTVHgLYDFtvirg md5 WordListJWT.txt 10`

At this point, the md5, sha256 and sha512 algorithms can be passed by argument. If a different hashing algorithm is used, it can be implemented without further complication.

# Description
The current script replicates the algorithm of the creation of a jwt and tries to find the "secret" used to sign the jwt. This script was created to solve a CTF challenge and was useful to understand the process of creating a jwt and changing the hash algorithm used.

We tried to keep the use of the script simple by leaving the possibility to create the jwt literally by command line, pass a wordlist and indicate the number of threads to use.

In addition to the main script, a secondary script was created to corroborate the correct creation of jwts, its use is the following:

`python3 build_jwt.py <jsonBody> <jsonPayload> <secret> <algorithm>`

Example:

`python3 build_jwt.py "{\"alg\":\"HS256\",\"typ\":\"JWT\"}" "{\"sub\":\"1234567890\",\"name\":\"John Doe\",\"iat\":151623902266}" admin md5`
