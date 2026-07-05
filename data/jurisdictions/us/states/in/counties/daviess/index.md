---
type: Jurisdiction
title: "Daviess County, IN"
classification: county
fips: "18027"
state: "IN"
demographics:
  population: 33658
  population_under_18: 10015
  population_18_64: 18259
  population_65_plus: 5384
  median_household_income: 68503
  poverty_rate: 11.67
  homeownership_rate: 72.39
  unemployment_rate: 1.55
  median_home_value: 197200
  gini_index: 0.4374
  vacancy_rate: 8.33
  race_white: 30161
  race_black: 555
  race_asian: 88
  race_native: 66
  hispanic: 2193
  bachelors_plus: 4329
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/senate/39"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/house/63"
    rel: in-district
    area_weight: 0.8343
  - to: "us/states/in/districts/house/45"
    rel: in-district
    area_weight: 0.1656
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Daviess County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33658 |
| Under 18 | 10015 |
| 18–64 | 18259 |
| 65+ | 5384 |
| Median household income | 68503 |
| Poverty rate | 11.67 |
| Homeownership rate | 72.39 |
| Unemployment rate | 1.55 |
| Median home value | 197200 |
| Gini index | 0.4374 |
| Vacancy rate | 8.33 |
| White | 30161 |
| Black | 555 |
| Asian | 88 |
| Native | 66 |
| Hispanic/Latino | 2193 |
| Bachelor's or higher | 4329 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 100% (congressional)
- [IN Senate District 39](/us/states/in/districts/senate/39.md) — 100% (state senate)
- [IN House District 63](/us/states/in/districts/house/63.md) — 83% (state house)
- [IN House District 45](/us/states/in/districts/house/45.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
