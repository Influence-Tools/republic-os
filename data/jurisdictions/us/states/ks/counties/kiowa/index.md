---
type: Jurisdiction
title: "Kiowa County, KS"
classification: county
fips: "20097"
state: "KS"
demographics:
  population: 2422
  population_under_18: 563
  population_18_64: 1311
  population_65_plus: 548
  median_household_income: 75539
  poverty_rate: 5.85
  homeownership_rate: 72.98
  unemployment_rate: 2.2
  median_home_value: 155300
  gini_index: 0.4578
  vacancy_rate: 17.17
  race_white: 2144
  race_black: 23
  race_asian: 66
  race_native: 10
  hispanic: 110
  bachelors_plus: 589
districts:
  - to: "us/states/ks/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/33"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/116"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Kiowa County, KS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2422 |
| Under 18 | 563 |
| 18–64 | 1311 |
| 65+ | 548 |
| Median household income | 75539 |
| Poverty rate | 5.85 |
| Homeownership rate | 72.98 |
| Unemployment rate | 2.2 |
| Median home value | 155300 |
| Gini index | 0.4578 |
| Vacancy rate | 17.17 |
| White | 2144 |
| Black | 23 |
| Asian | 66 |
| Native | 10 |
| Hispanic/Latino | 110 |
| Bachelor's or higher | 589 |

## Districts

- [KS-04](/us/states/ks/districts/04.md) — 100% (congressional)
- [KS Senate District 33](/us/states/ks/districts/senate/33.md) — 100% (state senate)
- [KS House District 116](/us/states/ks/districts/house/116.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
