---
type: Jurisdiction
title: "Bertie County, NC"
classification: county
fips: "37015"
state: "NC"
demographics:
  population: 17170
  population_under_18: 2788
  population_18_64: 10042
  population_65_plus: 4340
  median_household_income: 48750
  poverty_rate: 16.14
  homeownership_rate: 72.71
  unemployment_rate: 5.08
  median_home_value: 98500
  gini_index: 0.4876
  vacancy_rate: 20.49
  race_white: 5934
  race_black: 10238
  race_asian: 130
  race_native: 76
  hispanic: 422
  bachelors_plus: 3339
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.9648
  - to: "us/states/nc/districts/senate/1"
    rel: in-district
    area_weight: 0.9562
  - to: "us/states/nc/districts/house/23"
    rel: in-district
    area_weight: 0.9564
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Bertie County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17170 |
| Under 18 | 2788 |
| 18–64 | 10042 |
| 65+ | 4340 |
| Median household income | 48750 |
| Poverty rate | 16.14 |
| Homeownership rate | 72.71 |
| Unemployment rate | 5.08 |
| Median home value | 98500 |
| Gini index | 0.4876 |
| Vacancy rate | 20.49 |
| White | 5934 |
| Black | 10238 |
| Asian | 130 |
| Native | 76 |
| Hispanic/Latino | 422 |
| Bachelor's or higher | 3339 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 96% (congressional)
- [NC Senate District 1](/us/states/nc/districts/senate/1.md) — 96% (state senate)
- [NC House District 23](/us/states/nc/districts/house/23.md) — 96% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
