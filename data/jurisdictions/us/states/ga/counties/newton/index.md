---
type: Jurisdiction
title: "Newton County, GA"
classification: county
fips: "13217"
state: "GA"
demographics:
  population: 118152
  population_under_18: 29868
  population_18_64: 72414
  population_65_plus: 15870
  median_household_income: 77179
  poverty_rate: 12.29
  homeownership_rate: 73.77
  unemployment_rate: 6.64
  median_home_value: 265000
  gini_index: 0.4009
  vacancy_rate: 5.54
  race_white: 46820
  race_black: 56661
  race_asian: 1791
  race_native: 64
  hispanic: 8435
  bachelors_plus: 27008
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 0.7508
  - to: "us/states/ga/districts/13"
    rel: in-district
    area_weight: 0.2492
  - to: "us/states/ga/districts/senate/42"
    rel: in-district
    area_weight: 0.9571
  - to: "us/states/ga/districts/senate/43"
    rel: in-district
    area_weight: 0.0426
  - to: "us/states/ga/districts/house/114"
    rel: in-district
    area_weight: 0.4872
  - to: "us/states/ga/districts/house/118"
    rel: in-district
    area_weight: 0.3258
  - to: "us/states/ga/districts/house/113"
    rel: in-district
    area_weight: 0.1865
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Newton County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 118152 |
| Under 18 | 29868 |
| 18–64 | 72414 |
| 65+ | 15870 |
| Median household income | 77179 |
| Poverty rate | 12.29 |
| Homeownership rate | 73.77 |
| Unemployment rate | 6.64 |
| Median home value | 265000 |
| Gini index | 0.4009 |
| Vacancy rate | 5.54 |
| White | 46820 |
| Black | 56661 |
| Asian | 1791 |
| Native | 64 |
| Hispanic/Latino | 8435 |
| Bachelor's or higher | 27008 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 75% (congressional)
- [GA-13](/us/states/ga/districts/13.md) — 25% (congressional)
- [GA Senate District 42](/us/states/ga/districts/senate/42.md) — 96% (state senate)
- [GA Senate District 43](/us/states/ga/districts/senate/43.md) — 4% (state senate)
- [GA House District 114](/us/states/ga/districts/house/114.md) — 49% (state house)
- [GA House District 118](/us/states/ga/districts/house/118.md) — 33% (state house)
- [GA House District 113](/us/states/ga/districts/house/113.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
