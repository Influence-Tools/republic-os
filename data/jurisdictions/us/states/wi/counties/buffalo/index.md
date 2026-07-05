---
type: Jurisdiction
title: "Buffalo County, WI"
classification: county
fips: "55011"
state: "WI"
demographics:
  population: 13393
  population_under_18: 2668
  population_18_64: 7507
  population_65_plus: 3218
  median_household_income: 70479
  poverty_rate: 8.43
  homeownership_rate: 77.5
  unemployment_rate: 2.85
  median_home_value: 213300
  gini_index: 0.4043
  vacancy_rate: 12.3
  race_white: 12599
  race_black: 57
  race_asian: 33
  race_native: 29
  hispanic: 385
  bachelors_plus: 2816
districts:
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/senate/10"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/house/29"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Buffalo County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13393 |
| Under 18 | 2668 |
| 18–64 | 7507 |
| 65+ | 3218 |
| Median household income | 70479 |
| Poverty rate | 8.43 |
| Homeownership rate | 77.5 |
| Unemployment rate | 2.85 |
| Median home value | 213300 |
| Gini index | 0.4043 |
| Vacancy rate | 12.3 |
| White | 12599 |
| Black | 57 |
| Asian | 33 |
| Native | 29 |
| Hispanic/Latino | 385 |
| Bachelor's or higher | 2816 |

## Districts

- [WI-03](/us/states/wi/districts/03.md) — 100% (congressional)
- [WI Senate District 10](/us/states/wi/districts/senate/10.md) — 100% (state senate)
- [WI House District 29](/us/states/wi/districts/house/29.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
