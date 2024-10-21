# TODO

- Tiling:
    - [X] Create clean functions to generate a tiling
    - [X] Algorithm to repeat the tilings
    - [X] 1-uniform tilings
    - [ ] Fix duplication issue
    - [ ] Irregular polygon tilings
        - [ ] Shape => RegPolygon?
        - [ ] IrregPolygon object?
    - [ ] 2-uniform tilings
    - [ ] 3-uniform tilings & beyond

- Tight-Binding => Band Structure:
    - [X] Read about valence/electronic structure & solid state
    - [X] Integrate tight binding python package
        - [X] Generate a list of lattice vectors for a unit
        - [X] Specify vertex positions in lattice vector basis
        - [X] Plot the unit to see vertex/edge/vector indices
        - [X] Free energy and hopping parameters
        - [ ] The outer orbitals of the unit need to be able to hop to orbitals of the adjacent unit…
    - [X] Find equilibrium bond lengths? (Not needed, distance dependence is handled by hopping parameters)
    - [ ] Determine best k-space path (identify high-symmetry points in the k-space. typically located at special positions in the Brillouin zone that reflect the symmetry of the lattice)
    - [ ] Test on some known materials
    - [ ] Automatic classification of band structure

- Parallel Plane Rotations:
    - [ ] Tiling ⇒ Layer
        - [ ] Remove position and rotation from Layer?
    - [ ] Layers object. Can hold any number of layers, and can plot the layer tilings and layer units in 3d.
        - [ ] Can specify origin point for each layer as well as a rotation around a point
        - [ ] [layer, pos, rot]
