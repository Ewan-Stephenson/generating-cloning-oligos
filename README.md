# generating-cloning-oligos

The code here is a small project, currently only a few lines of code, intended to make ordering oligos for various CRISPR cloning methods easier. Most CRISPR systems require specific oligos with specific overlapping sequences or flanking regions for insert into the plasmid backbone. Ordering these is relatively fast, but it can still be sped up.

Currently the code allows ordering of oligos for basic cloning into LentiCRISPRv2, a CRISPR plasmid which is used for generating stable cell lines constituatively expressing Cas9 and the guide RNA. Eventually I wish to integrate this system with ordering systems eg IDT using web interfacing, but that will take some time. More likely is that, as I move into other backbones which need guides cloned into them, I will put here other tiny bits of code that might just make ordering the correct oligos slightly easier, all you need is your guide sequence.
