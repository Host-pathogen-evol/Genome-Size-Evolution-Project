
#Host-Pathogen system I-Genome length and jumps.

This is the latest incarnation of the effector-target genes evolution and genome
evolution.

## Recap.

We define a host and a pathogen by a set of attributes. The hosts are basically
an array of integers, taken from a pool of size $K_H$, whereas the pathogen are
labeled with integers from a pool of size $K_P$. For example, lets assume
$K_H=1000$ and $K_P=100$, if we form two sets of size $l_P=3$ and $l_H=5$ for
the pathogen and host respectively, then two possible *genomes* could be formed
by units labeled by numbers taken from those pools, e.g.:

$$g_P=\{e_{1},e_{2}, e_{2} \}=\{20,99,1\}$$ and
$$g_H=\{t_{1},t_{2},t_{3},t_{4},t_{5} \}=\{987,23,456,8,654\}$$

We say that a unit $e_n=i$ in the pathogen *interacts* with a unit $t_m=j$ in
the host with certain probability $c$. This defines and adjacency list (and a
Matrix for the full set of pathogen units) $A_{i,j}$ given by:


$$A_{i,j}=\left\{ \begin{array}{ll}
1 & \mbox{with  prob $c$}\\
0 & \mbox{with prob  $1-c$}.\end{array} \right.$$

In this model the list of integers and its length will suffice to describe the
Host. For the pathogen we consider more attributes in order to define the host-
pathogen interactions.

###Pathogen's genetic units attributes.

####Lenght
We are interested in the lenght evolution, hence the first attribute to
introduce is the unit's length. Every $e_i$ is accompannied by a real number
$l_i$ which stands for the units length. This number may vary in time as a the
consequence of an evolutionary event. Given a set of $N_g$ pathogenic units (a
genome $g$) the length $L_g$ is simply given by the sum over every unit present:
$$L_G=l_{e_1}+l_{e_2}+\dots+l_{e_{N_P}} \equiv \Sigma _{k=1}^{N_P}l_{e_k} $$

####Interaction scores and *Expression*

Alongside with the adjacency list, every *connection* is weighted according to a
given score $s_{ij}$ reflecting the fact that a given pathogen unit can improve
or worsen its efficiiency due to the number of connections present or as a
consequence of a mutational change. The scores are positive real numbers which
evolve as described in the next section. For now we introduce the *expression*
of a unit, which, as decribed below, is connected to the pathogen's reproduction
rate.

Let $\{s_{i,j}\}_{j=0}^{L_{H_P}}$ be the list of scores between unit i and the
host H. Then we define the expression of unit $i$, by:

$$ W_i=\frac{\alpha}{L_{H_P}c}\Sigma_{j=1}^{L_{H_P}}w_{ij}$$

Where $w_{ij}=\frac{s_{ij}^z}{s_{ij}^z+s_o^z}$ .


    
