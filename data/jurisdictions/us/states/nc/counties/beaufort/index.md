---
type: Jurisdiction
title: "Beaufort County, NC"
classification: county
fips: "37013"
state: "NC"
demographics:
  population: 44499
  population_under_18: 8515
  population_18_64: 24572
  population_65_plus: 11412
  median_household_income: 58357
  poverty_rate: 17.82
  homeownership_rate: 69.53
  unemployment_rate: 3.94
  median_home_value: 192700
  gini_index: 0.4646
  vacancy_rate: 20.96
  race_white: 30368
  race_black: 10166
  race_asian: 118
  race_native: 95
  hispanic: 3513
  bachelors_plus: 9294
districts:
  - to: "us/states/nc/districts/03"
    rel: in-district
    area_weight: 0.896
  - to: "us/states/nc/districts/senate/3"
    rel: in-district
    area_weight: 0.894
  - to: "us/states/nc/districts/house/79"
    rel: in-district
    area_weight: 0.894
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Beaufort County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 44499 |
| Under 18 | 8515 |
| 18–64 | 24572 |
| 65+ | 11412 |
| Median household income | 58357 |
| Poverty rate | 17.82 |
| Homeownership rate | 69.53 |
| Unemployment rate | 3.94 |
| Median home value | 192700 |
| Gini index | 0.4646 |
| Vacancy rate | 20.96 |
| White | 30368 |
| Black | 10166 |
| Asian | 118 |
| Native | 95 |
| Hispanic/Latino | 3513 |
| Bachelor's or higher | 9294 |

## Districts

- [NC-03](/us/states/nc/districts/03.md) — 90% (congressional)
- [NC Senate District 3](/us/states/nc/districts/senate/3.md) — 89% (state senate)
- [NC House District 79](/us/states/nc/districts/house/79.md) — 89% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
