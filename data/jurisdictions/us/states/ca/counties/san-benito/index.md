---
type: Jurisdiction
title: "San Benito County, CA"
classification: county
fips: "06069"
state: "CA"
demographics:
  population: 67290
  population_under_18: 17016
  population_18_64: 41040
  population_65_plus: 9234
  median_household_income: 114394
  poverty_rate: 6.67
  homeownership_rate: 67.94
  unemployment_rate: 5.38
  median_home_value: 793400
  gini_index: 0.4143
  vacancy_rate: 3.57
  race_white: 24620
  race_black: 639
  race_asian: 2646
  race_native: 1336
  hispanic: 41960
  bachelors_plus: 13693
districts:
  - to: "us/states/ca/districts/18"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ca/districts/senate/17"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ca/districts/house/29"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# San Benito County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 67290 |
| Under 18 | 17016 |
| 18–64 | 41040 |
| 65+ | 9234 |
| Median household income | 114394 |
| Poverty rate | 6.67 |
| Homeownership rate | 67.94 |
| Unemployment rate | 5.38 |
| Median home value | 793400 |
| Gini index | 0.4143 |
| Vacancy rate | 3.57 |
| White | 24620 |
| Black | 639 |
| Asian | 2646 |
| Native | 1336 |
| Hispanic/Latino | 41960 |
| Bachelor's or higher | 13693 |

## Districts

- [CA-18](/us/states/ca/districts/18.md) — 100% (congressional)
- [CA Senate District 17](/us/states/ca/districts/senate/17.md) — 100% (state senate)
- [CA House District 29](/us/states/ca/districts/house/29.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
