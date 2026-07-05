---
type: Jurisdiction
title: "Carteret County, NC"
classification: county
fips: "37031"
state: "NC"
demographics:
  population: 69148
  population_under_18: 11651
  population_18_64: 38832
  population_65_plus: 18665
  median_household_income: 72322
  poverty_rate: 10.07
  homeownership_rate: 74.69
  unemployment_rate: 4.03
  median_home_value: 333300
  gini_index: 0.4718
  vacancy_rate: 38.72
  race_white: 59438
  race_black: 2913
  race_asian: 692
  race_native: 173
  hispanic: 3401
  bachelors_plus: 25262
districts:
  - to: "us/states/nc/districts/03"
    rel: in-district
    area_weight: 0.4917
  - to: "us/states/nc/districts/senate/2"
    rel: in-district
    area_weight: 0.4246
  - to: "us/states/nc/districts/house/13"
    rel: in-district
    area_weight: 0.4246
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Carteret County, NC

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 69148 |
| Under 18 | 11651 |
| 18–64 | 38832 |
| 65+ | 18665 |
| Median household income | 72322 |
| Poverty rate | 10.07 |
| Homeownership rate | 74.69 |
| Unemployment rate | 4.03 |
| Median home value | 333300 |
| Gini index | 0.4718 |
| Vacancy rate | 38.72 |
| White | 59438 |
| Black | 2913 |
| Asian | 692 |
| Native | 173 |
| Hispanic/Latino | 3401 |
| Bachelor's or higher | 25262 |

## Districts

- [NC-03](/us/states/nc/districts/03.md) — 49% (congressional)
- [NC Senate District 2](/us/states/nc/districts/senate/2.md) — 42% (state senate)
- [NC House District 13](/us/states/nc/districts/house/13.md) — 42% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
