---
type: Jurisdiction
title: "Chaffee County, CO"
classification: county
fips: "08015"
state: "CO"
demographics:
  population: 20178
  population_under_18: 2804
  population_18_64: 12067
  population_65_plus: 5307
  median_household_income: 84132
  poverty_rate: 8.28
  homeownership_rate: 74.13
  unemployment_rate: 4.79
  median_home_value: 665700
  gini_index: 0.4186
  vacancy_rate: 14.1
  race_white: 17618
  race_black: 262
  race_asian: 108
  race_native: 59
  hispanic: 1983
  bachelors_plus: 10834
districts:
  - to: "us/states/co/districts/07"
    rel: in-district
    area_weight: 0.9965
  - to: "us/states/co/districts/senate/4"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/co/districts/house/13"
    rel: in-district
    area_weight: 0.8967
  - to: "us/states/co/districts/house/60"
    rel: in-district
    area_weight: 0.103
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Chaffee County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20178 |
| Under 18 | 2804 |
| 18–64 | 12067 |
| 65+ | 5307 |
| Median household income | 84132 |
| Poverty rate | 8.28 |
| Homeownership rate | 74.13 |
| Unemployment rate | 4.79 |
| Median home value | 665700 |
| Gini index | 0.4186 |
| Vacancy rate | 14.1 |
| White | 17618 |
| Black | 262 |
| Asian | 108 |
| Native | 59 |
| Hispanic/Latino | 1983 |
| Bachelor's or higher | 10834 |

## Districts

- [CO-07](/us/states/co/districts/07.md) — 100% (congressional)
- [CO Senate District 4](/us/states/co/districts/senate/4.md) — 100% (state senate)
- [CO House District 13](/us/states/co/districts/house/13.md) — 90% (state house)
- [CO House District 60](/us/states/co/districts/house/60.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
