---
type: Jurisdiction
title: "Sarasota County, FL"
classification: county
fips: "12115"
state: "FL"
demographics:
  population: 459547
  population_under_18: 64325
  population_18_64: 222860
  population_65_plus: 172362
  median_household_income: 83416
  poverty_rate: 8.59
  homeownership_rate: 76.71
  unemployment_rate: 3.74
  median_home_value: 411800
  gini_index: 0.5052
  vacancy_rate: 20.37
  race_white: 377661
  race_black: 18197
  race_asian: 8919
  race_native: 1418
  hispanic: 48971
  bachelors_plus: 213968
districts:
  - to: "us/states/fl/districts/17"
    rel: in-district
    area_weight: 0.6209
  - to: "us/states/fl/districts/senate/22"
    rel: in-district
    area_weight: 0.6207
  - to: "us/states/fl/districts/house/74"
    rel: in-district
    area_weight: 0.4278
  - to: "us/states/fl/districts/house/73"
    rel: in-district
    area_weight: 0.1105
  - to: "us/states/fl/districts/house/75"
    rel: in-district
    area_weight: 0.0823
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Sarasota County, FL

County jurisdiction — 39 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 459547 |
| Under 18 | 64325 |
| 18–64 | 222860 |
| 65+ | 172362 |
| Median household income | 83416 |
| Poverty rate | 8.59 |
| Homeownership rate | 76.71 |
| Unemployment rate | 3.74 |
| Median home value | 411800 |
| Gini index | 0.5052 |
| Vacancy rate | 20.37 |
| White | 377661 |
| Black | 18197 |
| Asian | 8919 |
| Native | 1418 |
| Hispanic/Latino | 48971 |
| Bachelor's or higher | 213968 |

## Districts

- [FL-17](/us/states/fl/districts/17.md) — 62% (congressional)
- [FL Senate District 22](/us/states/fl/districts/senate/22.md) — 62% (state senate)
- [FL House District 74](/us/states/fl/districts/house/74.md) — 43% (state house)
- [FL House District 73](/us/states/fl/districts/house/73.md) — 11% (state house)
- [FL House District 75](/us/states/fl/districts/house/75.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
