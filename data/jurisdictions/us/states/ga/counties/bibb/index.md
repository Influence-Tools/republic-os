---
type: Jurisdiction
title: "Bibb County, GA"
classification: county
fips: "13021"
state: "GA"
demographics:
  population: 156578
  population_under_18: 38203
  population_18_64: 92620
  population_65_plus: 25755
  median_household_income: 51234
  poverty_rate: 24.73
  homeownership_rate: 51.4
  unemployment_rate: 8.13
  median_home_value: 174500
  gini_index: 0.5216
  vacancy_rate: 16.73
  race_white: 55291
  race_black: 86013
  race_asian: 3590
  race_native: 281
  hispanic: 7371
  bachelors_plus: 40561
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.7666
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.2334
  - to: "us/states/ga/districts/senate/26"
    rel: in-district
    area_weight: 0.498
  - to: "us/states/ga/districts/senate/18"
    rel: in-district
    area_weight: 0.4543
  - to: "us/states/ga/districts/senate/25"
    rel: in-district
    area_weight: 0.0477
  - to: "us/states/ga/districts/house/145"
    rel: in-district
    area_weight: 0.3953
  - to: "us/states/ga/districts/house/143"
    rel: in-district
    area_weight: 0.3328
  - to: "us/states/ga/districts/house/142"
    rel: in-district
    area_weight: 0.1646
  - to: "us/states/ga/districts/house/149"
    rel: in-district
    area_weight: 0.0584
  - to: "us/states/ga/districts/house/144"
    rel: in-district
    area_weight: 0.0483
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Bibb County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 156578 |
| Under 18 | 38203 |
| 18–64 | 92620 |
| 65+ | 25755 |
| Median household income | 51234 |
| Poverty rate | 24.73 |
| Homeownership rate | 51.4 |
| Unemployment rate | 8.13 |
| Median home value | 174500 |
| Gini index | 0.5216 |
| Vacancy rate | 16.73 |
| White | 55291 |
| Black | 86013 |
| Asian | 3590 |
| Native | 281 |
| Hispanic/Latino | 7371 |
| Bachelor's or higher | 40561 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 77% (congressional)
- [GA-08](/us/states/ga/districts/08.md) — 23% (congressional)
- [GA Senate District 26](/us/states/ga/districts/senate/26.md) — 50% (state senate)
- [GA Senate District 18](/us/states/ga/districts/senate/18.md) — 45% (state senate)
- [GA Senate District 25](/us/states/ga/districts/senate/25.md) — 5% (state senate)
- [GA House District 145](/us/states/ga/districts/house/145.md) — 40% (state house)
- [GA House District 143](/us/states/ga/districts/house/143.md) — 33% (state house)
- [GA House District 142](/us/states/ga/districts/house/142.md) — 16% (state house)
- [GA House District 149](/us/states/ga/districts/house/149.md) — 6% (state house)
- [GA House District 144](/us/states/ga/districts/house/144.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
