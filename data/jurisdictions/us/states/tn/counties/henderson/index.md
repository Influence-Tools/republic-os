---
type: Jurisdiction
title: "Henderson County, TN"
classification: county
fips: "47077"
state: "TN"
demographics:
  population: 27980
  population_under_18: 6359
  population_18_64: 16497
  population_65_plus: 5124
  median_household_income: 55136
  poverty_rate: 16.85
  homeownership_rate: 73.19
  unemployment_rate: 6.1
  median_home_value: 164800
  gini_index: 0.4443
  vacancy_rate: 15.76
  race_white: 24389
  race_black: 2199
  race_asian: 45
  race_native: 37
  hispanic: 835
  bachelors_plus: 4150
districts:
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 0.9962
  - to: "us/states/tn/districts/senate/25"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tn/districts/house/79"
    rel: in-district
    area_weight: 0.5945
  - to: "us/states/tn/districts/house/72"
    rel: in-district
    area_weight: 0.4054
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Henderson County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27980 |
| Under 18 | 6359 |
| 18–64 | 16497 |
| 65+ | 5124 |
| Median household income | 55136 |
| Poverty rate | 16.85 |
| Homeownership rate | 73.19 |
| Unemployment rate | 6.1 |
| Median home value | 164800 |
| Gini index | 0.4443 |
| Vacancy rate | 15.76 |
| White | 24389 |
| Black | 2199 |
| Asian | 45 |
| Native | 37 |
| Hispanic/Latino | 835 |
| Bachelor's or higher | 4150 |

## Districts

- [TN-08](/us/states/tn/districts/08.md) — 100% (congressional)
- [TN Senate District 25](/us/states/tn/districts/senate/25.md) — 100% (state senate)
- [TN House District 79](/us/states/tn/districts/house/79.md) — 59% (state house)
- [TN House District 72](/us/states/tn/districts/house/72.md) — 41% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
