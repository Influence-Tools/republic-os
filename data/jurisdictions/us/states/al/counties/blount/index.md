---
type: Jurisdiction
title: "Blount County, AL"
classification: county
fips: "01009"
state: "AL"
demographics:
  population: 59518
  population_under_18: 13733
  population_18_64: 34718
  population_65_plus: 11067
  median_household_income: 64190
  poverty_rate: 12.86
  homeownership_rate: 80.98
  unemployment_rate: 5.0
  median_home_value: 175200
  gini_index: 0.4309
  vacancy_rate: 10.99
  race_white: 52460
  race_black: 716
  race_asian: 69
  race_native: 216
  hispanic: 6130
  bachelors_plus: 8985
districts:
  - to: "us/states/al/districts/04"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/al/districts/senate/17"
    rel: in-district
    area_weight: 0.7421
  - to: "us/states/al/districts/senate/9"
    rel: in-district
    area_weight: 0.2576
  - to: "us/states/al/districts/house/34"
    rel: in-district
    area_weight: 0.6626
  - to: "us/states/al/districts/house/11"
    rel: in-district
    area_weight: 0.3372
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Blount County, AL

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 59518 |
| Under 18 | 13733 |
| 18–64 | 34718 |
| 65+ | 11067 |
| Median household income | 64190 |
| Poverty rate | 12.86 |
| Homeownership rate | 80.98 |
| Unemployment rate | 5.0 |
| Median home value | 175200 |
| Gini index | 0.4309 |
| Vacancy rate | 10.99 |
| White | 52460 |
| Black | 716 |
| Asian | 69 |
| Native | 216 |
| Hispanic/Latino | 6130 |
| Bachelor's or higher | 8985 |

## Districts

- [AL-04](/us/states/al/districts/04.md) — 100% (congressional)
- [AL Senate District 17](/us/states/al/districts/senate/17.md) — 74% (state senate)
- [AL Senate District 9](/us/states/al/districts/senate/9.md) — 26% (state senate)
- [AL House District 34](/us/states/al/districts/house/34.md) — 66% (state house)
- [AL House District 11](/us/states/al/districts/house/11.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
