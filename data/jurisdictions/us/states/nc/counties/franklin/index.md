---
type: Jurisdiction
title: "Franklin County, NC"
classification: county
fips: "37069"
state: "NC"
demographics:
  population: 74386
  population_under_18: 16194
  population_18_64: 45204
  population_65_plus: 12988
  median_household_income: 74240
  poverty_rate: 11.06
  homeownership_rate: 78.59
  unemployment_rate: 4.61
  median_home_value: 284300
  gini_index: 0.429
  vacancy_rate: 10.19
  race_white: 45832
  race_black: 17406
  race_asian: 832
  race_native: 191
  hispanic: 8319
  bachelors_plus: 18700
districts:
  - to: "us/states/nc/districts/13"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/nc/districts/senate/11"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/7"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Franklin County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 74386 |
| Under 18 | 16194 |
| 18–64 | 45204 |
| 65+ | 12988 |
| Median household income | 74240 |
| Poverty rate | 11.06 |
| Homeownership rate | 78.59 |
| Unemployment rate | 4.61 |
| Median home value | 284300 |
| Gini index | 0.429 |
| Vacancy rate | 10.19 |
| White | 45832 |
| Black | 17406 |
| Asian | 832 |
| Native | 191 |
| Hispanic/Latino | 8319 |
| Bachelor's or higher | 18700 |

## Districts

- [NC-13](/us/states/nc/districts/13.md) — 100% (congressional)
- [NC Senate District 11](/us/states/nc/districts/senate/11.md) — 100% (state senate)
- [NC House District 7](/us/states/nc/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
