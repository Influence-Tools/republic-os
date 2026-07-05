---
type: Jurisdiction
title: "Texas County, OK"
classification: county
fips: "40139"
state: "OK"
demographics:
  population: 20774
  population_under_18: 5983
  population_18_64: 12258
  population_65_plus: 2533
  median_household_income: 60069
  poverty_rate: 15.72
  homeownership_rate: 66.41
  unemployment_rate: 3.43
  median_home_value: 163500
  gini_index: 0.4428
  vacancy_rate: 19.35
  race_white: 9648
  race_black: 1124
  race_asian: 296
  race_native: 717
  hispanic: 10816
  bachelors_plus: 3754
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ok/districts/senate/27"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ok/districts/house/61"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Texas County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20774 |
| Under 18 | 5983 |
| 18–64 | 12258 |
| 65+ | 2533 |
| Median household income | 60069 |
| Poverty rate | 15.72 |
| Homeownership rate | 66.41 |
| Unemployment rate | 3.43 |
| Median home value | 163500 |
| Gini index | 0.4428 |
| Vacancy rate | 19.35 |
| White | 9648 |
| Black | 1124 |
| Asian | 296 |
| Native | 717 |
| Hispanic/Latino | 10816 |
| Bachelor's or higher | 3754 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 27](/us/states/ok/districts/senate/27.md) — 100% (state senate)
- [OK House District 61](/us/states/ok/districts/house/61.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
