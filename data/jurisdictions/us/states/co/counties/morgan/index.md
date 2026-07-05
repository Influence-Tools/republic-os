---
type: Jurisdiction
title: "Morgan County, CO"
classification: county
fips: "08087"
state: "CO"
demographics:
  population: 29520
  population_under_18: 7368
  population_18_64: 17416
  population_65_plus: 4736
  median_household_income: 73278
  poverty_rate: 14.33
  homeownership_rate: 67.33
  unemployment_rate: 5.31
  median_home_value: 338600
  gini_index: 0.4195
  vacancy_rate: 6.23
  race_white: 18835
  race_black: 592
  race_asian: 219
  race_native: 661
  hispanic: 11348
  bachelors_plus: 4761
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/house/63"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Morgan County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29520 |
| Under 18 | 7368 |
| 18–64 | 17416 |
| 65+ | 4736 |
| Median household income | 73278 |
| Poverty rate | 14.33 |
| Homeownership rate | 67.33 |
| Unemployment rate | 5.31 |
| Median home value | 338600 |
| Gini index | 0.4195 |
| Vacancy rate | 6.23 |
| White | 18835 |
| Black | 592 |
| Asian | 219 |
| Native | 661 |
| Hispanic/Latino | 11348 |
| Bachelor's or higher | 4761 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 100% (congressional)
- [CO Senate District 1](/us/states/co/districts/senate/1.md) — 100% (state senate)
- [CO House District 63](/us/states/co/districts/house/63.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
