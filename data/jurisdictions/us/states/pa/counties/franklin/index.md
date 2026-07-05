---
type: Jurisdiction
title: "Franklin County, PA"
classification: county
fips: "42055"
state: "PA"
demographics:
  population: 157379
  population_under_18: 34556
  population_18_64: 91048
  population_65_plus: 31775
  median_household_income: 77003
  poverty_rate: 8.48
  homeownership_rate: 73.52
  unemployment_rate: 3.99
  median_home_value: 249800
  gini_index: 0.4132
  vacancy_rate: 5.43
  race_white: 136565
  race_black: 4870
  race_asian: 1632
  race_native: 590
  hispanic: 11830
  bachelors_plus: 38750
districts:
  - to: "us/states/pa/districts/13"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/pa/districts/senate/33"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/pa/districts/house/90"
    rel: in-district
    area_weight: 0.4065
  - to: "us/states/pa/districts/house/81"
    rel: in-district
    area_weight: 0.3979
  - to: "us/states/pa/districts/house/89"
    rel: in-district
    area_weight: 0.1953
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Franklin County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 157379 |
| Under 18 | 34556 |
| 18–64 | 91048 |
| 65+ | 31775 |
| Median household income | 77003 |
| Poverty rate | 8.48 |
| Homeownership rate | 73.52 |
| Unemployment rate | 3.99 |
| Median home value | 249800 |
| Gini index | 0.4132 |
| Vacancy rate | 5.43 |
| White | 136565 |
| Black | 4870 |
| Asian | 1632 |
| Native | 590 |
| Hispanic/Latino | 11830 |
| Bachelor's or higher | 38750 |

## Districts

- [PA-13](/us/states/pa/districts/13.md) — 100% (congressional)
- [PA Senate District 33](/us/states/pa/districts/senate/33.md) — 100% (state senate)
- [PA House District 90](/us/states/pa/districts/house/90.md) — 41% (state house)
- [PA House District 81](/us/states/pa/districts/house/81.md) — 40% (state house)
- [PA House District 89](/us/states/pa/districts/house/89.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
