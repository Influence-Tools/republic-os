---
type: Jurisdiction
title: "Carver County, MN"
classification: county
fips: "27019"
state: "MN"
demographics:
  population: 110041
  population_under_18: 27759
  population_18_64: 66275
  population_65_plus: 16007
  median_household_income: 125946
  poverty_rate: 4.42
  homeownership_rate: 81.48
  unemployment_rate: 3.06
  median_home_value: 453600
  gini_index: 0.4224
  vacancy_rate: 2.59
  race_white: 95342
  race_black: 1830
  race_asian: 3678
  race_native: 258
  hispanic: 5624
  bachelors_plus: 49515
districts:
  - to: "us/states/mn/districts/06"
    rel: in-district
    area_weight: 0.9974
  - to: "us/states/mn/districts/senate/17"
    rel: in-district
    area_weight: 0.5975
  - to: "us/states/mn/districts/senate/48"
    rel: in-district
    area_weight: 0.4023
  - to: "us/states/mn/districts/house/17b"
    rel: in-district
    area_weight: 0.5975
  - to: "us/states/mn/districts/house/48a"
    rel: in-district
    area_weight: 0.3119
  - to: "us/states/mn/districts/house/48b"
    rel: in-district
    area_weight: 0.0904
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Carver County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 110041 |
| Under 18 | 27759 |
| 18–64 | 66275 |
| 65+ | 16007 |
| Median household income | 125946 |
| Poverty rate | 4.42 |
| Homeownership rate | 81.48 |
| Unemployment rate | 3.06 |
| Median home value | 453600 |
| Gini index | 0.4224 |
| Vacancy rate | 2.59 |
| White | 95342 |
| Black | 1830 |
| Asian | 3678 |
| Native | 258 |
| Hispanic/Latino | 5624 |
| Bachelor's or higher | 49515 |

## Districts

- [MN-06](/us/states/mn/districts/06.md) — 100% (congressional)
- [MN Senate District 17](/us/states/mn/districts/senate/17.md) — 60% (state senate)
- [MN Senate District 48](/us/states/mn/districts/senate/48.md) — 40% (state senate)
- [MN House District 17B](/us/states/mn/districts/house/17b.md) — 60% (state house)
- [MN House District 48A](/us/states/mn/districts/house/48a.md) — 31% (state house)
- [MN House District 48B](/us/states/mn/districts/house/48b.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
