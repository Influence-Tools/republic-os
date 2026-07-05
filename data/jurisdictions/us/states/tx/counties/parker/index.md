---
type: Jurisdiction
title: "Parker County, TX"
classification: county
fips: "48367"
state: "TX"
demographics:
  population: 165168
  population_under_18: 40730
  population_18_64: 98083
  population_65_plus: 26355
  median_household_income: 104443
  poverty_rate: 7.98
  homeownership_rate: 80.74
  unemployment_rate: 3.98
  median_home_value: 375900
  gini_index: 0.4403
  vacancy_rate: 5.75
  race_white: 137359
  race_black: 2158
  race_asian: 1443
  race_native: 744
  hispanic: 24246
  bachelors_plus: 48006
districts:
  - to: "us/states/tx/districts/12"
    rel: in-district
    area_weight: 0.6595
  - to: "us/states/tx/districts/25"
    rel: in-district
    area_weight: 0.3404
  - to: "us/states/tx/districts/senate/10"
    rel: in-district
    area_weight: 0.5964
  - to: "us/states/tx/districts/senate/30"
    rel: in-district
    area_weight: 0.4035
  - to: "us/states/tx/districts/house/60"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Parker County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 165168 |
| Under 18 | 40730 |
| 18–64 | 98083 |
| 65+ | 26355 |
| Median household income | 104443 |
| Poverty rate | 7.98 |
| Homeownership rate | 80.74 |
| Unemployment rate | 3.98 |
| Median home value | 375900 |
| Gini index | 0.4403 |
| Vacancy rate | 5.75 |
| White | 137359 |
| Black | 2158 |
| Asian | 1443 |
| Native | 744 |
| Hispanic/Latino | 24246 |
| Bachelor's or higher | 48006 |

## Districts

- [TX-12](/us/states/tx/districts/12.md) — 66% (congressional)
- [TX-25](/us/states/tx/districts/25.md) — 34% (congressional)
- [TX Senate District 10](/us/states/tx/districts/senate/10.md) — 60% (state senate)
- [TX Senate District 30](/us/states/tx/districts/senate/30.md) — 40% (state senate)
- [TX House District 60](/us/states/tx/districts/house/60.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
