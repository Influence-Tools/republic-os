---
type: Jurisdiction
title: "Davis County, IA"
classification: county
fips: "19051"
state: "IA"
demographics:
  population: 9157
  population_under_18: 2737
  population_18_64: 4759
  population_65_plus: 1661
  median_household_income: 77194
  poverty_rate: 7.16
  homeownership_rate: 83.26
  unemployment_rate: 2.72
  median_home_value: 161900
  gini_index: 0.3981
  vacancy_rate: 11.38
  race_white: 8642
  race_black: 0
  race_asian: 1
  race_native: 15
  hispanic: 223
  bachelors_plus: 1271
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/ia/districts/senate/13"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/26"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Davis County, IA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9157 |
| Under 18 | 2737 |
| 18–64 | 4759 |
| 65+ | 1661 |
| Median household income | 77194 |
| Poverty rate | 7.16 |
| Homeownership rate | 83.26 |
| Unemployment rate | 2.72 |
| Median home value | 161900 |
| Gini index | 0.3981 |
| Vacancy rate | 11.38 |
| White | 8642 |
| Black | 0 |
| Asian | 1 |
| Native | 15 |
| Hispanic/Latino | 223 |
| Bachelor's or higher | 1271 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 13](/us/states/ia/districts/senate/13.md) — 100% (state senate)
- [IA House District 26](/us/states/ia/districts/house/26.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
