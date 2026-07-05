---
type: Jurisdiction
title: "Delta County, CO"
classification: county
fips: "08029"
state: "CO"
demographics:
  population: 31598
  population_under_18: 6029
  population_18_64: 16596
  population_65_plus: 8973
  median_household_income: 57774
  poverty_rate: 13.99
  homeownership_rate: 77.94
  unemployment_rate: 3.15
  median_home_value: 343200
  gini_index: 0.4756
  vacancy_rate: 13.75
  race_white: 26665
  race_black: 216
  race_asian: 167
  race_native: 195
  hispanic: 4571
  bachelors_plus: 8412
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/5"
    rel: in-district
    area_weight: 0.827
  - to: "us/states/co/districts/senate/7"
    rel: in-district
    area_weight: 0.173
  - to: "us/states/co/districts/house/54"
    rel: in-district
    area_weight: 0.5018
  - to: "us/states/co/districts/house/58"
    rel: in-district
    area_weight: 0.4982
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Delta County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31598 |
| Under 18 | 6029 |
| 18–64 | 16596 |
| 65+ | 8973 |
| Median household income | 57774 |
| Poverty rate | 13.99 |
| Homeownership rate | 77.94 |
| Unemployment rate | 3.15 |
| Median home value | 343200 |
| Gini index | 0.4756 |
| Vacancy rate | 13.75 |
| White | 26665 |
| Black | 216 |
| Asian | 167 |
| Native | 195 |
| Hispanic/Latino | 4571 |
| Bachelor's or higher | 8412 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 5](/us/states/co/districts/senate/5.md) — 83% (state senate)
- [CO Senate District 7](/us/states/co/districts/senate/7.md) — 17% (state senate)
- [CO House District 54](/us/states/co/districts/house/54.md) — 50% (state house)
- [CO House District 58](/us/states/co/districts/house/58.md) — 50% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
