---
type: Jurisdiction
title: "Montrose County, CO"
classification: county
fips: "08085"
state: "CO"
demographics:
  population: 43807
  population_under_18: 8775
  population_18_64: 23632
  population_65_plus: 11400
  median_household_income: 72120
  poverty_rate: 11.52
  homeownership_rate: 75.39
  unemployment_rate: 4.4
  median_home_value: 388400
  gini_index: 0.437
  vacancy_rate: 8.55
  race_white: 33994
  race_black: 215
  race_asian: 206
  race_native: 527
  hispanic: 9427
  bachelors_plus: 12685
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/co/districts/senate/6"
    rel: in-district
    area_weight: 0.7217
  - to: "us/states/co/districts/senate/5"
    rel: in-district
    area_weight: 0.2781
  - to: "us/states/co/districts/house/58"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Montrose County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43807 |
| Under 18 | 8775 |
| 18–64 | 23632 |
| 65+ | 11400 |
| Median household income | 72120 |
| Poverty rate | 11.52 |
| Homeownership rate | 75.39 |
| Unemployment rate | 4.4 |
| Median home value | 388400 |
| Gini index | 0.437 |
| Vacancy rate | 8.55 |
| White | 33994 |
| Black | 215 |
| Asian | 206 |
| Native | 527 |
| Hispanic/Latino | 9427 |
| Bachelor's or higher | 12685 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 6](/us/states/co/districts/senate/6.md) — 72% (state senate)
- [CO Senate District 5](/us/states/co/districts/senate/5.md) — 28% (state senate)
- [CO House District 58](/us/states/co/districts/house/58.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
