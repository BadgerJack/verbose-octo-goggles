Anatomy of a Block
==================
The anatomy of a typical block in the chain consists of 6 lines.

Ballot: __genesis   # This is the most important information - who has been voted for.

VoterID: 12345      # This is the unique identity of the voter. It is unique, but randomly selected to maintain anonymity.

Hash: 123           # The file hash is calculated based on the ballot, voterID, and height. This ensures it remains unique. As the hash is only used for integrity purposes, there is no need for anything stronger than MD5.

Previous Hash: 555  # The hash of the previous file is stored here. This maintains the linked chain of files.

Height: 0           # The height of the file is how many files above the genesis block have been created. This correlates to how many votes have been cast.

Nonce: 12345        # The nonce is a random number used in salting. It is not currently used, but has been left in for future expansion.

End of File
