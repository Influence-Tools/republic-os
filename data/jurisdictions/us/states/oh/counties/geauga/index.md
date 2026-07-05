---
type: Jurisdiction
title: "Geauga County, OH"
classification: county
fips: "39055"
state: "OH"
demographics:
  population: 95481
  population_under_18: 21185
  population_18_64: 53007
  population_65_plus: 21289
  median_household_income: 107860
  poverty_rate: 5.57
  homeownership_rate: 87.18
  unemployment_rate: 2.97
  median_home_value: 331100
  gini_index: 0.4496
  vacancy_rate: 5.06
  race_white: 88963
  race_black: 922
  race_asian: 478
  race_native: 42
  hispanic: 1868
  bachelors_plus: 37847
districts:
  - to: "us/states/oh/districts/14"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/oh/districts/senate/32"
    rel: in-district
    area_weight: 0.8541
  - to: "us/states/oh/districts/senate/27"
    rel: in-district
    area_weight: 0.1458
  - to: "us/states/oh/districts/house/99"
    rel: in-district
    area_weight: 0.8541
  - to: "us/states/oh/districts/house/35"
    rel: in-district
    area_weight: 0.1458
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Geauga County, OH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 95481 |
| Under 18 | 21185 |
| 18–64 | 53007 |
| 65+ | 21289 |
| Median household income | 107860 |
| Poverty rate | 5.57 |
| Homeownership rate | 87.18 |
| Unemployment rate | 2.97 |
| Median home value | 331100 |
| Gini index | 0.4496 |
| Vacancy rate | 5.06 |
| White | 88963 |
| Black | 922 |
| Asian | 478 |
| Native | 42 |
| Hispanic/Latino | 1868 |
| Bachelor's or higher | 37847 |

## Districts

- [OH-14](/us/states/oh/districts/14.md) — 100% (congressional)
- [OH Senate District 32](/us/states/oh/districts/senate/32.md) — 85% (state senate)
- [OH Senate District 27](/us/states/oh/districts/senate/27.md) — 15% (state senate)
- [OH House District 99](/us/states/oh/districts/house/99.md) — 85% (state house)
- [OH House District 35](/us/states/oh/districts/house/35.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
