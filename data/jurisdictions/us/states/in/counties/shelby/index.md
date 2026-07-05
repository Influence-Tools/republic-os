---
type: Jurisdiction
title: "Shelby County, IN"
classification: county
fips: "18145"
state: "IN"
demographics:
  population: 45265
  population_under_18: 10169
  population_18_64: 26655
  population_65_plus: 8441
  median_household_income: 72190
  poverty_rate: 13.04
  homeownership_rate: 72.46
  unemployment_rate: 3.56
  median_home_value: 212400
  gini_index: 0.4271
  vacancy_rate: 6.22
  race_white: 41272
  race_black: 626
  race_asian: 455
  race_native: 67
  hispanic: 2549
  bachelors_plus: 9260
districts:
  - to: "us/states/in/districts/06"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/42"
    rel: in-district
    area_weight: 0.6019
  - to: "us/states/in/districts/senate/28"
    rel: in-district
    area_weight: 0.3979
  - to: "us/states/in/districts/house/47"
    rel: in-district
    area_weight: 0.501
  - to: "us/states/in/districts/house/73"
    rel: in-district
    area_weight: 0.4325
  - to: "us/states/in/districts/house/54"
    rel: in-district
    area_weight: 0.0664
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Shelby County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 45265 |
| Under 18 | 10169 |
| 18–64 | 26655 |
| 65+ | 8441 |
| Median household income | 72190 |
| Poverty rate | 13.04 |
| Homeownership rate | 72.46 |
| Unemployment rate | 3.56 |
| Median home value | 212400 |
| Gini index | 0.4271 |
| Vacancy rate | 6.22 |
| White | 41272 |
| Black | 626 |
| Asian | 455 |
| Native | 67 |
| Hispanic/Latino | 2549 |
| Bachelor's or higher | 9260 |

## Districts

- [IN-06](/us/states/in/districts/06.md) — 100% (congressional)
- [IN Senate District 42](/us/states/in/districts/senate/42.md) — 60% (state senate)
- [IN Senate District 28](/us/states/in/districts/senate/28.md) — 40% (state senate)
- [IN House District 47](/us/states/in/districts/house/47.md) — 50% (state house)
- [IN House District 73](/us/states/in/districts/house/73.md) — 43% (state house)
- [IN House District 54](/us/states/in/districts/house/54.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
