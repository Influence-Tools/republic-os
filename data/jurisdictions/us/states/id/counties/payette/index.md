---
type: Jurisdiction
title: "Payette County, ID"
classification: county
fips: "16075"
state: "ID"
demographics:
  population: 26771
  population_under_18: 6826
  population_18_64: 14657
  population_65_plus: 5288
  median_household_income: 67673
  poverty_rate: 10.19
  homeownership_rate: 74.5
  unemployment_rate: 3.2
  median_home_value: 341800
  gini_index: 0.3909
  vacancy_rate: 4.43
  race_white: 21960
  race_black: 30
  race_asian: 196
  race_native: 223
  hispanic: 4790
  bachelors_plus: 4085
districts:
  - to: "us/states/id/districts/01"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/id/districts/senate/9"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Payette County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26771 |
| Under 18 | 6826 |
| 18–64 | 14657 |
| 65+ | 5288 |
| Median household income | 67673 |
| Poverty rate | 10.19 |
| Homeownership rate | 74.5 |
| Unemployment rate | 3.2 |
| Median home value | 341800 |
| Gini index | 0.3909 |
| Vacancy rate | 4.43 |
| White | 21960 |
| Black | 30 |
| Asian | 196 |
| Native | 223 |
| Hispanic/Latino | 4790 |
| Bachelor's or higher | 4085 |

## Districts

- [ID-01](/us/states/id/districts/01.md) — 100% (congressional)
- [ID Senate District 9](/us/states/id/districts/senate/9.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
