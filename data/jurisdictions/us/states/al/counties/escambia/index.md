---
type: Jurisdiction
title: "Escambia County, AL"
classification: county
fips: "01053"
state: "AL"
demographics:
  population: 36629
  population_under_18: 8308
  population_18_64: 21366
  population_65_plus: 6955
  median_household_income: 48225
  poverty_rate: 20.02
  homeownership_rate: 70.95
  unemployment_rate: 10.05
  median_home_value: 136500
  gini_index: 0.4649
  vacancy_rate: 23.83
  race_white: 22148
  race_black: 10831
  race_asian: 165
  race_native: 1040
  hispanic: 862
  bachelors_plus: 4805
districts:
  - to: "us/states/al/districts/01"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/al/districts/senate/22"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/al/districts/house/66"
    rel: in-district
    area_weight: 0.6782
  - to: "us/states/al/districts/house/92"
    rel: in-district
    area_weight: 0.3211
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Escambia County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36629 |
| Under 18 | 8308 |
| 18–64 | 21366 |
| 65+ | 6955 |
| Median household income | 48225 |
| Poverty rate | 20.02 |
| Homeownership rate | 70.95 |
| Unemployment rate | 10.05 |
| Median home value | 136500 |
| Gini index | 0.4649 |
| Vacancy rate | 23.83 |
| White | 22148 |
| Black | 10831 |
| Asian | 165 |
| Native | 1040 |
| Hispanic/Latino | 862 |
| Bachelor's or higher | 4805 |

## Districts

- [AL-01](/us/states/al/districts/01.md) — 100% (congressional)
- [AL Senate District 22](/us/states/al/districts/senate/22.md) — 100% (state senate)
- [AL House District 66](/us/states/al/districts/house/66.md) — 68% (state house)
- [AL House District 92](/us/states/al/districts/house/92.md) — 32% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
