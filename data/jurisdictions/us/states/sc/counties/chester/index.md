---
type: Jurisdiction
title: "Chester County, SC"
classification: county
fips: "45023"
state: "SC"
demographics:
  population: 32182
  population_under_18: 7183
  population_18_64: 18810
  population_65_plus: 6189
  median_household_income: 52458
  poverty_rate: 18.68
  homeownership_rate: 78.43
  unemployment_rate: 5.56
  median_home_value: 158300
  gini_index: 0.4413
  vacancy_rate: 11.13
  race_white: 18737
  race_black: 11183
  race_asian: 126
  race_native: 49
  hispanic: 974
  bachelors_plus: 4357
districts:
  - to: "us/states/sc/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sc/districts/senate/17"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sc/districts/house/43"
    rel: in-district
    area_weight: 0.731
  - to: "us/states/sc/districts/house/41"
    rel: in-district
    area_weight: 0.2689
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Chester County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32182 |
| Under 18 | 7183 |
| 18–64 | 18810 |
| 65+ | 6189 |
| Median household income | 52458 |
| Poverty rate | 18.68 |
| Homeownership rate | 78.43 |
| Unemployment rate | 5.56 |
| Median home value | 158300 |
| Gini index | 0.4413 |
| Vacancy rate | 11.13 |
| White | 18737 |
| Black | 11183 |
| Asian | 126 |
| Native | 49 |
| Hispanic/Latino | 974 |
| Bachelor's or higher | 4357 |

## Districts

- [SC-05](/us/states/sc/districts/05.md) — 100% (congressional)
- [SC Senate District 17](/us/states/sc/districts/senate/17.md) — 100% (state senate)
- [SC House District 43](/us/states/sc/districts/house/43.md) — 73% (state house)
- [SC House District 41](/us/states/sc/districts/house/41.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
