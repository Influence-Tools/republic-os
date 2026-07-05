---
type: Jurisdiction
title: "Randolph County, IL"
classification: county
fips: "17157"
state: "IL"
demographics:
  population: 30058
  population_under_18: 6063
  population_18_64: 17602
  population_65_plus: 6393
  median_household_income: 68131
  poverty_rate: 14.63
  homeownership_rate: 76.58
  unemployment_rate: 5.04
  median_home_value: 135100
  gini_index: 0.4079
  vacancy_rate: 11.0
  race_white: 25786
  race_black: 2497
  race_asian: 169
  race_native: 191
  hispanic: 1147
  bachelors_plus: 4443
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/il/districts/senate/58"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/il/districts/house/115"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Randolph County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30058 |
| Under 18 | 6063 |
| 18–64 | 17602 |
| 65+ | 6393 |
| Median household income | 68131 |
| Poverty rate | 14.63 |
| Homeownership rate | 76.58 |
| Unemployment rate | 5.04 |
| Median home value | 135100 |
| Gini index | 0.4079 |
| Vacancy rate | 11.0 |
| White | 25786 |
| Black | 2497 |
| Asian | 169 |
| Native | 191 |
| Hispanic/Latino | 1147 |
| Bachelor's or higher | 4443 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 58](/us/states/il/districts/senate/58.md) — 100% (state senate)
- [IL House District 115](/us/states/il/districts/house/115.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
