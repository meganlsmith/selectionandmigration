---
title: SLiM
theme: minima
---

# Simple Models

First we consider a set of models with constant mutation rates, constant recombination rates, and relatively simple DFEs.

## Demographic models
1. No migration (nomig)
2. Migration P1 -> P2 (p1_p2)
3. Migration P2 -> P1 (p2_p1)

## Distributions of Fitness Effects
1. Neutral ([neutral-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/nomig_neutral_scaled.slim), [neutral-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p1_p2_neutral_scaled.slim), [neutral-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p2_p1_neutral_scaled.slim))
2. Simple Background Selection ([bgs-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/nomig_bgs_scaled.slim), [bgs-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p1_p2_bgs_scaled.slim), [bgs-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p2_p1_bgs_scaled.slim))
3. Selective Sweep in P1 ([linkedp1-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/nomig_linkedp1_scaled.slim), [linkedp1-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p1_p2_linkedp1_scaled.slim), [linkedp1-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p2_p1_linkedp1_scaled.slim))
4. Selective Sweep in the ancestor ([linkedancestor-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/nomig_linkedancestor_scaled.slim), [linkedancestor-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p1_p2_linkedancestor_scaled.slim), [linkedancestor-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p2_p1_linkedancestor_scaled.slim))
5. Adaptive Introgression ([adaptiveint-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/nomig_adaptiveint_scaled.slim), [adaptiveint-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p1_p2_adaptiveint_scaled.slim), [adaptiveint-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p2_p1_adaptiveint_scaled.slim))
