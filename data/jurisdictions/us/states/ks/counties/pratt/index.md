---
type: Jurisdiction
title: "Pratt County, KS"
classification: county
fips: "20151"
state: "KS"
demographics:
  population: 9127
  population_under_18: 2253
  population_18_64: 4946
  population_65_plus: 1928
  median_household_income: 66022
  poverty_rate: 12.3
  homeownership_rate: 73.24
  unemployment_rate: 3.6
  median_home_value: 114600
  gini_index: 0.4287
  vacancy_rate: 20.53
  race_white: 7801
  race_black: 59
  race_asian: 22
  race_native: 79
  hispanic: 788
  bachelors_plus: 2079
districts:
  - to: "us/states/ks/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/33"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/116"
    rel: in-district
    area_weight: 0.5254
  - to: "us/states/ks/districts/house/114"
    rel: in-district
    area_weight: 0.4746
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Pratt County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9127 |
| Under 18 | 2253 |
| 18–64 | 4946 |
| 65+ | 1928 |
| Median household income | 66022 |
| Poverty rate | 12.3 |
| Homeownership rate | 73.24 |
| Unemployment rate | 3.6 |
| Median home value | 114600 |
| Gini index | 0.4287 |
| Vacancy rate | 20.53 |
| White | 7801 |
| Black | 59 |
| Asian | 22 |
| Native | 79 |
| Hispanic/Latino | 788 |
| Bachelor's or higher | 2079 |

## Districts

- [KS-04](/us/states/ks/districts/04.md) — 100% (congressional)
- [KS Senate District 33](/us/states/ks/districts/senate/33.md) — 100% (state senate)
- [KS House District 116](/us/states/ks/districts/house/116.md) — 53% (state house)
- [KS House District 114](/us/states/ks/districts/house/114.md) — 47% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
