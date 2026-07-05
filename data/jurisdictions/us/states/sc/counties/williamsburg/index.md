---
type: Jurisdiction
title: "Williamsburg County, SC"
classification: county
fips: "45089"
state: "SC"
demographics:
  population: 30282
  population_under_18: 5882
  population_18_64: 17533
  population_65_plus: 6867
  median_household_income: 46213
  poverty_rate: 23.33
  homeownership_rate: 76.37
  unemployment_rate: 3.96
  median_home_value: 104500
  gini_index: 0.4987
  vacancy_rate: 17.55
  race_white: 9950
  race_black: 19185
  race_asian: 238
  race_native: 145
  hispanic: 758
  bachelors_plus: 5354
districts:
  - to: "us/states/sc/districts/06"
    rel: in-district
    area_weight: 0.9957
  - to: "us/states/sc/districts/senate/32"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/sc/districts/house/101"
    rel: in-district
    area_weight: 0.8096
  - to: "us/states/sc/districts/house/57"
    rel: in-district
    area_weight: 0.1902
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Williamsburg County, SC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30282 |
| Under 18 | 5882 |
| 18–64 | 17533 |
| 65+ | 6867 |
| Median household income | 46213 |
| Poverty rate | 23.33 |
| Homeownership rate | 76.37 |
| Unemployment rate | 3.96 |
| Median home value | 104500 |
| Gini index | 0.4987 |
| Vacancy rate | 17.55 |
| White | 9950 |
| Black | 19185 |
| Asian | 238 |
| Native | 145 |
| Hispanic/Latino | 758 |
| Bachelor's or higher | 5354 |

## Districts

- [SC-06](/us/states/sc/districts/06.md) — 100% (congressional)
- [SC Senate District 32](/us/states/sc/districts/senate/32.md) — 100% (state senate)
- [SC House District 101](/us/states/sc/districts/house/101.md) — 81% (state house)
- [SC House District 57](/us/states/sc/districts/house/57.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
