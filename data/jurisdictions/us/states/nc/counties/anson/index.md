---
type: Jurisdiction
title: "Anson County, NC"
classification: county
fips: "37007"
state: "NC"
demographics:
  population: 22289
  population_under_18: 4426
  population_18_64: 13468
  population_65_plus: 4395
  median_household_income: 47302
  poverty_rate: 21.73
  homeownership_rate: 68.52
  unemployment_rate: 5.5
  median_home_value: 148600
  gini_index: 0.4636
  vacancy_rate: 14.12
  race_white: 9911
  race_black: 10031
  race_asian: 351
  race_native: 129
  hispanic: 932
  bachelors_plus: 2044
districts:
  - to: "us/states/nc/districts/08"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nc/districts/senate/29"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/55"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Anson County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22289 |
| Under 18 | 4426 |
| 18–64 | 13468 |
| 65+ | 4395 |
| Median household income | 47302 |
| Poverty rate | 21.73 |
| Homeownership rate | 68.52 |
| Unemployment rate | 5.5 |
| Median home value | 148600 |
| Gini index | 0.4636 |
| Vacancy rate | 14.12 |
| White | 9911 |
| Black | 10031 |
| Asian | 351 |
| Native | 129 |
| Hispanic/Latino | 932 |
| Bachelor's or higher | 2044 |

## Districts

- [NC-08](/us/states/nc/districts/08.md) — 100% (congressional)
- [NC Senate District 29](/us/states/nc/districts/senate/29.md) — 100% (state senate)
- [NC House District 55](/us/states/nc/districts/house/55.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
