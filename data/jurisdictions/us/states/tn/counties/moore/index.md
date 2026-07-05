---
type: Jurisdiction
title: "Moore County, TN"
classification: county
fips: "47127"
state: "TN"
demographics:
  population: 6674
  population_under_18: 1307
  population_18_64: 3890
  population_65_plus: 1477
  median_household_income: 66469
  poverty_rate: 8.05
  homeownership_rate: 82.51
  unemployment_rate: 4.49
  median_home_value: 285300
  gini_index: 0.4105
  vacancy_rate: 9.21
  race_white: 6181
  race_black: 144
  race_asian: 39
  race_native: 3
  hispanic: 140
  bachelors_plus: 1658
districts:
  - to: "us/states/tn/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/senate/14"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/tn/districts/house/62"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Moore County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6674 |
| Under 18 | 1307 |
| 18–64 | 3890 |
| 65+ | 1477 |
| Median household income | 66469 |
| Poverty rate | 8.05 |
| Homeownership rate | 82.51 |
| Unemployment rate | 4.49 |
| Median home value | 285300 |
| Gini index | 0.4105 |
| Vacancy rate | 9.21 |
| White | 6181 |
| Black | 144 |
| Asian | 39 |
| Native | 3 |
| Hispanic/Latino | 140 |
| Bachelor's or higher | 1658 |

## Districts

- [TN-04](/us/states/tn/districts/04.md) — 100% (congressional)
- [TN Senate District 14](/us/states/tn/districts/senate/14.md) — 100% (state senate)
- [TN House District 62](/us/states/tn/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
