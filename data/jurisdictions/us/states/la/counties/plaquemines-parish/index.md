---
type: Jurisdiction
title: "Plaquemines Parish, LA"
classification: county
fips: "22075"
state: "LA"
demographics:
  population: 22803
  population_under_18: 5616
  population_18_64: 13966
  population_65_plus: 3221
  median_household_income: 86315
  poverty_rate: 12.88
  homeownership_rate: 75.8
  unemployment_rate: 4.22
  median_home_value: 282900
  gini_index: 0.4132
  vacancy_rate: 15.59
  race_white: 13692
  race_black: 4811
  race_asian: 797
  race_native: 298
  hispanic: 2227
  bachelors_plus: 4350
districts:
  - to: "us/states/la/districts/01"
    rel: in-district
    area_weight: 0.5141
  - to: "us/states/la/districts/senate/7"
    rel: in-district
    area_weight: 0.2766
  - to: "us/states/la/districts/senate/8"
    rel: in-district
    area_weight: 0.1877
  - to: "us/states/la/districts/house/105"
    rel: in-district
    area_weight: 0.4642
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Plaquemines Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22803 |
| Under 18 | 5616 |
| 18–64 | 13966 |
| 65+ | 3221 |
| Median household income | 86315 |
| Poverty rate | 12.88 |
| Homeownership rate | 75.8 |
| Unemployment rate | 4.22 |
| Median home value | 282900 |
| Gini index | 0.4132 |
| Vacancy rate | 15.59 |
| White | 13692 |
| Black | 4811 |
| Asian | 797 |
| Native | 298 |
| Hispanic/Latino | 2227 |
| Bachelor's or higher | 4350 |

## Districts

- [LA-01](/us/states/la/districts/01.md) — 51% (congressional)
- [LA Senate District 7](/us/states/la/districts/senate/7.md) — 28% (state senate)
- [LA Senate District 8](/us/states/la/districts/senate/8.md) — 19% (state senate)
- [LA House District 105](/us/states/la/districts/house/105.md) — 46% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
